# Чтобы интегрировать возможность вызова kernel_panic() при ошибке, нужно подключить его и вызвать kernel_panic(str(error)) в exception
# Ниже вы можете видеть пример кода:

# from kernel_panic import kernel_panic;

# try:
#     print(10/0)
# except Exception as error:
#     kernel_panic(str(error))

def kernel_panic(error):
    print(f"""
---------Kernel panic---------

Система не может работать из-за фатальной ошибки
          
Возможные шаги решения проблемы:
1. Попробуйте перезапустить TripleOS
2. Если это не помогло, попробуйте переустановить систему с нуля

Ошибка:
{error}

------------------------------
""")