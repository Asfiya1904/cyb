import streamlit as st
import os
import json
from typing import Dict, Any
from time import sleep
import random

# Simulated integration test function (replace with your actual logic)
def run_integration_test(output_dir: str = "./reports") -> Dict[str, Any]:
    os.makedirs(output_dir, exist_ok=True)
    st.info("Running integration test...")
    sleep(2)

    test_report = {
        "phishing_detected": random.choice([True, False]),
        "malware_detected": random.choice([True, False]),
        "ransomware_detected": random.choice([True, False]),
        "overall_status": "pass" if random.random() > 0.2 else "fail"
    }

    performance_report = {
        "cpu_usage": f"{random.randint(10, 50)}%",
        "memory_usage": f"{random.randint(200, 700)}MB",
        "latency_ms": random.randint(50, 200)
    }

    test_path = os.path.join(output_dir, "test_report.json")
    perf_path = os.path.join(output_dir, "performance_report.json")

    with open(test_path, "w") as f:
        json.dump(test_report, f, indent=2)

    with open(perf_path, "w") as f:
        json.dump(performance_report, f, indent=2)

    return {
        "success": test_report["overall_status"] == "pass",
        "test_report": test_report,
        "performance_report": performance_report
    }

# Streamlit UI
st.set_page_config(page_title="DefenSys – AI Threat Detection", page_icon="🛡️")
st.title("🛡️ DefenSys: AI-Powered Threat Detection")

if st.button("Run Integration Test"):
    result = run_integration_test("reports")

    st.success("✅ Integration Test Complete")
    st.subheader("🧪 Test Results")
    st.json(result['test_report'])

    st.subheader("📊 Performance Metrics")
    st.json(result['performance_report'])
