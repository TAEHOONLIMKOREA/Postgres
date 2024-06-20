import psycopg2
from psycopg2 import sql

def insert_test_data():
    # 데이터베이스 연결 설정
    connection = psycopg2.connect(
        host='bigsoft.iptime.org',    # 데이터베이스 서버 주소
        port='55422',
        database='keti_3pdx',  # 데이터베이스 이름
        user='keti_root',       # 데이터베이스 사용자 이름
        password='madcoder')   # 사용자 비밀번호

    # 커서 생성
    cursor = connection.cursor()

    # 스키마 생성
    cursor.execute("CREATE SCHEMA IF NOT EXISTS my_schema;")

    # 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_schema.my_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT
        );
    """)

    # 데이터 삽입 쿼리
    insert_query = sql.SQL("""
        INSERT INTO my_schema.my_table (name, age)
        VALUES (%s, %s)
    """)

    # 삽입할 데이터
    test_data = [
        ('John Doe', 30),
        ('Jane Smith', 25),
        ('Alice Johnson', 35)
    ]

    # 데이터 삽입
    try:
        for data in test_data:
            cursor.execute(insert_query, data)
        connection.commit()  # 변경사항 저장
        print("Schema created, table created, and data inserted successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()  # 오류 발생 시 롤백
    finally:
        # 커넥션 닫기
        cursor.close()
        connection.close()

# 함수 실행
if __name__ == '__main__':
    insert_test_data()
