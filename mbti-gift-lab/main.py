from crew_logic import MbtiLoopCrew

if __name__ == "__main__":
    print("--- Welcome to MBTI Gift Lab ---")
    user_mbti = input("Enter the MBTI type (e.g., INFP, ESTJ, INTJ): ").upper()
    
    crew = MbtiLoopCrew()
    result = crew.run(user_mbti)
    
    print("\n\n########################")
    print("## FINAL SIMULATION ##")
    print("########################\n")
    print(result)