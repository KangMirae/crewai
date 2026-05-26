from crew_logic import MbtiLoopCrew

if __name__ == "__main__":
    print("--- Bienvenido a MBTI Gift Lab ---")
    user_mbti = input("Introduce el tipo MBTI (ej. INFP, ESTJ, INTJ): ").upper()
    
    crew = MbtiLoopCrew()
    result = crew.run(user_mbti)
    
    print("\n\n############################")
    print("## RESULTADO FINAL ##")
    print("############################\n")
    print(result)
