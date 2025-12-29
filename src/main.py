from LLM import generate_sql
from db import run_sql

def main():
    print("嗨~~我是你的電信資料查詢助手")
    print("輸入 exit 可以離開唷!")

    while True:
        q = input("\n今天想問什麼呢？> ").strip()
        if q.lower() in ("exit", "quit"):
            break

        sql = generate_sql(q)
        print("\n[SQL]")
        print(sql)

        try:
            cols, rows = run_sql(sql)
            print("\n[Result]")
            if cols:
                print(" | ".join(cols))
                print("-" * 60)
            for r in rows[:30]:
                print(r)
            if len(rows) > 30:
                print(f"... ({len(rows)} rows)")
        except Exception as e:
            print("\n SQL 執行失敗：", e)

if __name__ == "__main__":
    main()
