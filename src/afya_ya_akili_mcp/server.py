"""AfyaYaAkiliMCP — Kenya Mental Health Resources (5 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP
mcp = FastMCP(name="afya-ya-akili-mcp", instructions="Kenya mental health resources. DEMO data only. If in crisis: Befrienders Kenya 0800 723 253.")

@mcp.tool(name="mental_health_provider_finder", description="Find licensed mental health practitioners in Kenya by county. DEMO.")
def mental_health_provider_finder(county: Optional[str] = None, provider_type: Optional[str] = None) -> dict:
    TYPES = {"psychiatrist": "Medical doctor specialising in mental health. Prescribes medication.",
             "psychologist":  "Assesses and provides therapy. Cannot prescribe medication in Kenya.",
             "counselor":     "KCPA/KCA registered counsellor. Talk therapy, shorter training.",
             "psychotherapist":"Longer-term talk therapy. Various modalities (CBT, psychodynamic)."}
    RESOURCES = [
        {"name": "Mathare Hospital", "type": "public_hospital", "county": "Nairobi",
         "note": "Kenya's main public psychiatric hospital. NHIF accredited.", "contact": "020-2001000"},
        {"name": "Chiromo Lane Medical Centre", "type": "private_clinic", "county": "Nairobi",
         "note": "Comprehensive psychiatric care. Private.", "contact": "020-2014469"},
        {"name": "Befrienders Kenya", "type": "crisis_support", "county": "Nairobi",
         "note": "Emotional support for distress/suicidal thoughts. Free. Confidential.", "contact": "0800 723 253"},
        {"name": "Aga Khan University Hospital — Psychiatry", "type": "private_hospital", "county": "Nairobi",
         "note": "Outpatient and inpatient psychiatry. NHIF for some cases.", "contact": "020-3662000"},
        {"name": "USIU-Africa Counselling Centre", "type": "training_clinic", "county": "Nairobi",
         "note": "Affordable counselling by supervised trainees.", "contact": "020-3606000"},
    ]
    if county:
        RESOURCES = [r for r in RESOURCES if county.lower() in r["county"].lower()]
    if provider_type:
        RESOURCES = [r for r in RESOURCES if provider_type.lower() in r["type"]] or RESOURCES
    return {"source": "DEMO — Kenya Psychiatric Association, KCA", "county": county,
            "resources": RESOURCES, "kpa": "Kenya Psychiatric Association: psychiatry.or.ke",
            "kca": "Kenya Counsellors Association: kcaglobal.com",
            "nhif": "NHIF covers inpatient psychiatric care at accredited facilities"}

@mcp.tool(name="crisis_line_directory", description="Kenya mental health crisis lines and emergency resources. DEMO.")
def crisis_line_directory() -> dict:
    return {"source": "DEMO — verified crisis lines", "emergency": "If life is at risk: 999 or nearest hospital",
            "crisis_lines": [
                {"name": "Befrienders Kenya", "number": "0800 723 253", "hours": "24/7",
                 "note": "Free. Confidential. Emotional support for distress, suicidal thoughts."},
                {"name": "CCAK (Churches Community Counselling Association)",
                 "number": "0722 178 177", "hours": "Business hours",
                 "note": "Christian counselling. Also serves non-Christians."},
                {"name": "Chiromo Lane Medical", "number": "0722 178 177",
                 "hours": "24-hour psychiatric emergencies", "note": "Private. Charges apply."},
                {"name": "Mathare Hospital (emergency)", "number": "020-2001000",
                 "hours": "24/7 emergency", "note": "Public hospital. No charges for emergency."},
            ],
            "text_support": "iCall Kenya: icallhelpline.org (online chat, Mon-Sat)",
            "note": "If you or someone you know is in immediate danger, go to the nearest hospital emergency department."}

@mcp.tool(name="mental_health_rights", description="Mental health rights under Kenya Mental Health Act 2022. DEMO.")
def mental_health_rights(topic: Optional[str] = None) -> dict:
    RIGHTS = {
        "consent":        "No person may be admitted or treated without free and informed consent, except under emergency or court order.",
        "confidentiality":"Mental health records are confidential. Cannot be disclosed without consent (subject to safety exceptions).",
        "voluntary":      "Right to seek voluntary treatment without involuntary admission.",
        "dignity":        "Right to be treated with dignity. No cruel treatment in mental health facilities.",
        "appeal":         "Involuntary admission can be appealed to the Mental Health Tribunal within 7 days.",
        "community":      "Right to community-based mental health care, not just institutional.",
        "discrimination": "Disability Discrimination Act protects people with mental health conditions from employment discrimination.",
        "insurance":      "Insurance companies cannot deny coverage solely on mental health history under 2022 Act.",
    }
    if topic:
        t = topic.lower()
        matched = {k: v for k, v in RIGHTS.items() if k in t or any(w in t for w in k.split("_"))}
        return {"source": "DEMO — Kenya Mental Health Act 2022", "topic": topic,
                "rights": matched or RIGHTS, "disclaimer": "Not legal advice."}
    return {"source": "DEMO — Kenya Mental Health Act 2022 (kenyalaw.org)", "rights": RIGHTS,
            "regulator": "Mental Health Tribunal. Kenya Medical Practitioners & Dentists Council (KMPDC)."}

@mcp.tool(name="workplace_wellness_guide", description="Kenya workplace mental health policies and EAP programs. DEMO.")
def workplace_wellness_guide(query: Optional[str] = None) -> dict:
    INFO = {
        "legal_obligation": "Employers have duty of care under Occupational Safety & Health Act 2007. Mental health included.",
        "eap":              "Employee Assistance Programs: Chiromo Lane, Minet Kenya, UAP Old Mutual offer EAP packages. Cost: KES 500-2000/employee/year.",
        "stress_leave":     "No specific 'mental health leave' in Kenya law. Use sick leave (7 days statutory). Doctor's note required.",
        "burnout_guide":    "Burnout is not a medical diagnosis in Kenya yet. Manage as occupational stress under OSHA.",
        "policies":         "Create mental health policy: awareness, confidentiality, accommodation, EAP, manager training.",
        "reduce_stigma":    "Training managers to recognize signs. Anonymous wellness surveys. Normalise 'mental health days'.",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — DOSH Kenya, DOSHS", "query": query, "guidance": matched or INFO}
    return {"source": "DEMO — Kenya Occupational Safety & Health Act 2007", "guidance": INFO,
            "dosh": "Directorate of Occupational Safety and Health Services: doshs.go.ke"}

@mcp.tool(name="self_help_resources", description="Kenya mental health self-help resources and support groups. DEMO.")
def self_help_resources(area: Optional[str] = None) -> dict:
    return {"source": "DEMO — Kenya mental health organizations", "area": area,
            "online_resources": [
                {"name": "Niskize", "url": "niskize.com", "description": "Kenya mental health awareness, articles, provider directory"},
                {"name": "iCall Kenya", "url": "icallhelpline.org", "description": "Online counselling, Mon-Sat"},
                {"name": "WHO Mental Health Atlas Kenya", "url": "who.int", "description": "Country-level mental health data"},
            ],
            "support_groups": [
                {"name": "Anxiety & Depression Support Kenya", "platform": "Facebook (private group)",
                 "description": "Peer support community"},
                {"name": "KCPA Patient Support", "description": "Kenya Psychiatric Association patient forums"},
                {"name": "AA Kenya", "description": "Alcoholics Anonymous Kenya: aaKenya.org"},
            ],
            "self_care": ["Regular exercise (even 20-min walk reduces anxiety)", "Sleep hygiene",
                          "Social connection — invest in 2-3 strong relationships",
                          "Limit social media consumption during stressful periods",
                          "Mindfulness: Headspace/Calm apps available free tier"],
            "when_to_seek_help": "Seek professional help if symptoms persist 2+ weeks or significantly affect daily functioning."}
