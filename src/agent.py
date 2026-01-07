import os
import sys
import time

def agent_response(text):
    print(f"\n[Opencode Thinking...]")
    time.sleep(1) # Thinking effect
    # This is a placeholder for actual LLM integration
    if "상태" in text or "status" in text:
        print("에이전트: 현재 시스템 상태는 양호합니다. 'vstatus'를 통해 상세 수치를 확인하실 수 있습니다.")
    elif "안녕" in text or "hi" in text:
        print("에이전트: 안녕하세요! 모바일에서 접속 중이시군요. 무엇을 도와드릴까요?")
    elif "커밋" in text or "sync" in text:
        print("에이전트: 'vsync' 명령어를 입력하시면 현재 변경사항을 깃허브에 바로 올릴 수 있습니다.")
    else:
        print(f"에이전트: '{text}'에 대한 요청을 확인했습니다. 현재는 브릿지 모드입니다.")
        print("실제 자율 코딩을 시작하려면 API Key를 시스템 환경 변수에 등록해 주세요.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("      🤖 OPENCODE AI AGENT : VIBE EDITION")
    print("="*50)
    print(" (Type 'exit' or '종료' to quit)")
    
    # Check for API Key (For future usage)
    has_api = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not has_api:
        print("\n⚠️  Notice: Brain (API Key) not connected.")
        print("   Set OPENAI_API_KEY to unlock full autonomous power.")
    
    while True:
        try:
            prompt = input("\n[User @ Mobile]> ")
            if prompt.lower() in ['exit', 'quit', '종료', '나가기']:
                print("\n에이전트: 접속을 종료합니다. 다음에 봬요!")
                break
            
            if not prompt.strip():
                continue
            
            agent_response(prompt)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
