def is_teacher_suspicious(self, n, tasks):
    last_task = ''
    for task in tasks:
        if task == last_task:
            continue
        elif task < last_task:
            return "NO"
        last_task = task
    return "YES"

def check_suspicion(self):
    t = int(input())

    for _ in range(t):
        n = int(input())
        tasks = input().upper()

        result = self.is_teacher_suspicious(n, tasks)
        print(result)
