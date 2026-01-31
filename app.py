import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from modules.parser import extract_text
from modules.nlp_engine import detect_language, extract_entities
from modules.clause_engine import extract_clauses, classify_contract
from modules.risk_engine import analyze_clause, contract_risk_score
from modules.llm_engine import explain_clause, generate_summary
from modules.template_engine import generate_employment_template
from modules.audit import save_audit
from modules.report_generator import generate_pdf_report

st.set_page_config(layout="wide")
st.title("⚖️ GenAI Contract Risk Assessment for Indian SMEs")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)

    contract_type = classify_contract(text)
    language = detect_language(text)
    entities = extract_entities(text)
    clauses = extract_clauses(text)

    st.subheader("📌 Contract Type")
    st.write(contract_type)

    st.subheader("🌐 Language")
    st.write(language)

    st.subheader("🏷 Extracted Entities")
    st.write(entities[:10])

    results = []

    for clause in clauses:
        risk, issues = analyze_clause(clause)
        explanation = explain_clause(clause)

        with st.expander(f"Risk: {risk}"):
            st.write(clause)
            st.write("Issues:", issues)
            st.write(explanation)

        results.append({"risk": risk})

    overall = contract_risk_score(results)

    st.subheader("📊 Overall Risk Score")
    st.write(overall)

    summary = generate_summary(text)
    st.subheader("📝 Contract Summary")
    st.write(summary)

    generate_pdf_report("report.pdf", summary)
    st.download_button("Download Report", open("report.pdf", "rb"))

    save_audit({
        "file": uploaded_file.name,
        "contract_type": contract_type,
        "risk": overall,
        "language": language
    })

st.sidebar.header("SME Contract Templates")
if st.sidebar.button("Employment Template"):
    st.sidebar.text(generate_employment_template())
