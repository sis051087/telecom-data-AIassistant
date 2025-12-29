from openai import OpenAI

SCHEMA = """
SQLite table: mobile_usage
Columns:
- year INTEGER
- month INTEGER
- operator TEXT
- avg_gb REAL

Rules:
- Output ONLY ONE SQL query.
- SELECT only (read-only).
- Only query table mobile_usage.
- Prefer avg_gb for analysis.
"""

def generate_sql(question: str , client: OpenAI ) -> str:
  # 展示用(Repo未包含API Key)
  prompt = f"""
Convert the user's Chinese question into SQLite SQL.

{SCHEMA}

Question: {question}

Return SQL only.
"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    sql = resp.choices[0].message.content.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql
