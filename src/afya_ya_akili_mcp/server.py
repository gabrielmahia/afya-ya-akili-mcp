"""AfyaYaAkiliMCP — Kenya Mental Health Resources (5 tools). All data DEMO."""
from __future__ import annotations

from typing import Optional

from fastmcp import FastMCP

# Annotations tell clients which tools are safe to auto-approve (read-only, no side effects).
READ_ONLY = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False}

mcp = FastMCP(name="afya-ya-akili-mcp", instructions="Kenya mental health resources, hand-compiled and partly unverified (read each answer's source). Not a substitute for emergency or clinical care. If life is at risk call 999 or 112. Befrienders Kenya: +254 722 178 177 (call, SMS or WhatsApp; Mon-Fri 9am-5pm). Kenya Red Cross: 1199.")

@mcp.tool(name="mental_health_provider_finder", description="Find licensed mental health practitioners in Kenya by county. DEMO.", annotations=READ_ONLY)
def mental_health_provider_finder(county: str | None = None, provider_type: str | None = None) -> dict:
    TYPES = {"psychiatrist": "Medical doctor specialising in mental health. Prescribes medication.",
             "psychologist":  "Assesses and provides therapy. Cannot prescribe medication in Kenya.",
             "counselor":     "KCPA/KCA registered counsellor. Talk therapy, shorter training.",
             "psychotherapist":"Longer-term talk therapy. Various modalities (CBT, psychodynamic)."}
    RESOURCES = [
        {"name": "Mathare Hospital", "type": "public_hospital", "county": "Nairobi",
         "note": "Kenya's main public psychiatric hospital. SHA accreditation status UNVERIFIED.", "contact": "020-2001000"},
        {"name": "Chiromo Lane Medical Centre", "type": "private_clinic", "county": "Nairobi",
         "note": "Comprehensive psychiatric care. Private.", "contact": "020-2014469"},
        {"name": "Befrienders Kenya", "type": "crisis_support", "county": "Nairobi",
         "note": "Emotional support for distress or suicidal thoughts. Free and confidential. Call, SMS or WhatsApp; Mon-Fri 9am-5pm per its own listing, not 24/7.", "contact": "+254 722 178 177"},
        {"name": "Aga Khan University Hospital — Psychiatry", "type": "private_hospital", "county": "Nairobi",
         "note": "Outpatient and inpatient psychiatry. SHA cover for some cases (UNVERIFIED).", "contact": "020-3662000"},
        {"name": "USIU-Africa Counselling Centre", "type": "training_clinic", "county": "Nairobi",
         "note": "Affordable counselling by supervised trainees.", "contact": "020-3606000"},
    ]
    if county:
        RESOURCES = [r for r in RESOURCES if county.lower() in r["county"].lower()]
    if provider_type:
        RESOURCES = [r for r in RESOURCES if provider_type.lower() in r["type"]] or RESOURCES
    return {"source": "DEMO — hand-compiled. Phone numbers other than Befrienders Kenya's (verified 2026-10-07) are NOT verified: confirm before use", "county": county,
            "resources": RESOURCES, "provider_type_guide": TYPES, "kpa": "Kenya Psychiatric Association: psychiatry.or.ke",
            "kca": "Kenya Counsellors Association: kcaglobal.com",
            "nhif": "Inpatient psychiatric care may be covered through SHA (which replaced NHIF in Oct 2024); scope UNVERIFIED, check sha.go.ke"}

@mcp.tool(name="crisis_line_directory", description="Kenya emergency and mental health crisis lines, compiled from public listings on 2026-10-07: number, hours, channels, and how many independent listings confirm each. Numbers change: confirm before relying. Not a substitute for emergency services.", annotations=READ_ONLY)
def crisis_line_directory() -> dict:
    return {
        "source": "Compiled from public listings on 2026-10-07: Befrienders Kenya's own listing via Lifeline International and Find A Helpline; Kenya Red Cross and emergency numbers via HapaKenya and Standard Media; NACADA and the child helpline via Find A Helpline. Numbers change: confirm before relying.",
        "emergency": "If life is at risk call 999 or 112 (911 also connects from Safaricom), or go to the nearest hospital emergency department.",
        "crisis_lines": [
            {"name": "Befrienders Kenya", "number": "+254 722 178 177", "channels": "call, SMS, WhatsApp", "cost": "free",
             "hours": "Mon-Fri 9am-5pm per its own listing (one other listing says 7am-7pm); NOT 24/7", "listings_confirming": 4,
             "note": "Free, confidential emotional support for distress, self-harm and suicidal thoughts. Outside these hours use 999/112, 1199 or a hospital emergency department."},
            {"name": "Kenya Red Cross", "number": "1199", "channels": "call", "cost": "toll-free", "hours": "24/7 per HapaKenya (2026-03)", "listings_confirming": 3,
             "note": "Toll-free humanitarian line; listed as a free national mental health helpline."},
            {"name": "Police and general emergency", "number": "999 or 112 (911 from Safaricom)", "channels": "call", "cost": "toll-free", "hours": "24/7", "listings_confirming": 2,
             "note": "Fire, ambulance and police."},
            {"name": "NACADA", "number": "1192", "channels": "call", "cost": "toll-free", "hours": "24-hour per OpenCounseling", "listings_confirming": 3,
             "note": "Alcohol and drug abuse."},
            {"name": "National Child Helpline", "number": "116", "channels": "call", "cost": "free", "hours": "24/7 per Find A Helpline", "listings_confirming": 2,
             "note": "Children and young people."},
            {"name": "Emergency Medicine Kenya Foundation", "number": "0800 723 253", "channels": "call", "cost": "toll-free", "hours": "not stated", "listings_confirming": 2,
             "note": "Listed under crisis lines by two secondary listings only: confirm. This is NOT Befrienders Kenya's number (earlier versions of this server attached it to Befrienders)."},
            {"name": "Gender Violence Recovery Centre", "number": "0800 720 565", "channels": "call", "cost": "toll-free", "hours": "not stated", "listings_confirming": 1,
             "note": "Gender-based violence. Single listing (TherapyRoute): confirm."},
        ],
        "not_included": "Earlier versions listed other numbers, an online counselling service that is not Kenyan, and a '24-hour psychiatric emergency' line that reused Befrienders' number; none could be verified, so they were removed.",
        "note": "If you or someone you know is in immediate danger, go to the nearest hospital emergency department.",
    }


@mcp.tool(name="mental_health_rights", description="Mental health rights under Kenya Mental Health Act 2022. DEMO.", annotations=READ_ONLY)
def mental_health_rights(topic: str | None = None) -> dict:
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

@mcp.tool(name="workplace_wellness_guide", description="Kenya workplace mental health policies and EAP programs. DEMO.", annotations=READ_ONLY)
def workplace_wellness_guide(query: str | None = None) -> dict:
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

@mcp.tool(name="self_help_resources", description="Kenya mental health self-help resources and support groups. DEMO.", annotations=READ_ONLY)
def self_help_resources(area: str | None = None) -> dict:
    return {"source": "DEMO — Kenya mental health organizations", "area": area,
            "online_resources": [
                {"name": "Niskize", "url": "niskize.com", "description": "Kenya mental health awareness, articles, provider directory"},
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

def main() -> None:
    """Console entry point."""
    mcp.run()
