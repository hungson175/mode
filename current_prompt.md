I know that we SHOULD NOT modify system prompt or TodoWrite description whatsoever. 
HOWEVER:
**Current** Khi sử dụng model LLM là grok-code-fast-1 (hiện tượng này không gặp khi dùng LLM là  claude sonnet !), parameter của TodoWrite (todos ấy) ở các lần 2,3,4... được gọi không phải là full list mà chỉ có 1-2 items của full todos - thực ra coding agent vẫn work, nhưng sẽ không ổn khi project quá dài, agent có thể "quên" full todo list (Forget in-the-middle) - chú thích: lần gọi đầu tiên của TodoWrite sẽ tạo ra full todo list thì vẫn ổn ngay cả trên grok-code-fast-1 LLM - another note: nếu dùng claude sonnet thì vẫn ổn cả
**Expected** Tất cả các lần gọi sau khi todo được lập bởi TodoWrite (2,3,4 ...), todo items vẫn phải full (kể cả trạng thái completed )


**Your task** - thay đổi ít nhất có thể nhưng phải nhấn mạnh chuyện này trong System Prompt và TodoWrite description

Đưa tôi review "before"/"after" SP & TodoWrite desc BEFORE you change anything !
