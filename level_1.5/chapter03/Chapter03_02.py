# 날짜 및 시간 포맷

from datetime import datetime, timezone

print(datetime.now(timezone.utc))
print()

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p'))
print()

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p %A %B'))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %p %a %b'))
print()

print(datetime.now().strftime('%A, %B %d, %Y %H:%M:%S'))
print(datetime.now().strftime('%A, %B %d, %Y %T'))
print()

print(datetime.now().strftime('%A, %b, %x %r'))