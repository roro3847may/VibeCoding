import os
import sys

def main():
    print("🤖 Opencode Terminal Agent (Vibe Coding Edition)")
    print("Type your request in Korean or English (type 'exit' to quit)")
    print("-" * 50)
    
    # Check for API Key
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️ Warning: No API Key found in environment variables.")
        print("Please set OPENAI_API_KEY to enable full autonomous features.")
    
    while True:
        try:
            user_input = input("Opencode> ")
            if user_input.lower() in ['exit', 'quit', '나가기', '종료']:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            # Logic for processing input will be added here
            print(f"\n[에이전트 사고 중...]: '{user_input}'")
            print("현재는 브릿지 모드입니다. API Key가 연결되면 실제 자율 코딩이 시작됩니다.")
            print("-" * 30)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
