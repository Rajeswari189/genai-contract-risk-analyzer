import streamlit as st
import matplotlib.pyplot as plt
from modules.parser import extract_text
from modules.nlp_engine import detect_language, extract_entities
from modules.clause_engine import extract_clauses, classify_contract
from modules.risk_engine import analyze_clause, contract_risk_score
from modules.llm_engine import explain_clause, generate_summary
from modules.report_generator import generate_pdf_report
from modules.audit import save_audit

st.set_page_config(layout="wide")
st.title("⚖️ GenAI Contract Risk Assessment for Indian SMEs")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)

    if not text.strip():
        st.warning("Empty document.")
        st.stop()

    contract_type = classify_contract(text)
    entities = extract_entities(text)
    clauses = extract_clauses(text)

    st.subheader("📌 Contract Type")
    st.write(contract_type)

    st.subheader("🏷 Key Entities")
    st.write(entities[:10])

    results = []
    risk_counts = {"Low": 0, "Medium": 0, "High": 0}

    for clause in clauses:
        risk, issues, numeric_score = analyze_clause(clause)
        explanation = explain_clause(clause)

        risk_counts[risk] += 1

        with st.expander(f"Risk: {risk}"):
            st.write(clause)
            st.write("Issues:", issues)
            st.write(explanation)

        results.append({
            "risk": risk,
            "numeric_score": numeric_score
        })

    overall = contract_risk_score(results)

    st.subheader("📊 Overall Risk Level")
    st.write(overall)

    st.subheader("📈 Risk Distribution")
    fig = plt.figure()
    plt.bar(risk_counts.keys(), risk_counts.values())
    st.pyplot(fig)

    summary = generate_summary(text)

    st.subheader("📝 Simplified Summary")
    st.write(summary)

    generate_pdf_report("report.pdf", summary, overall)
    st.download_button("Download PDF Report", open("report.pdf", "rb"))

    save_audit({
        "file": uploaded_file.name,
        "contract_type": contract_type,
        "overall_risk": overall,
        "total_clauses": len(clauses)
    })
