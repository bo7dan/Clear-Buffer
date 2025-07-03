import pyperclip
from rich.console import Console

console = Console()

ASCII_ART = """
[green]
░█▀▀░█░░░█▀▀░█▀█░█▀▄░░░░░█▀▄░█░█░█▀▀░█▀▀░█▀▀░█▀▄
░█░░░█░░░█▀▀░█▀█░█▀▄░░░░░█▀▄░█░█░█▀▀░█▀▀░█▀▀░█▀▄
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░░▀▀▀░▀░░░▀░░░▀▀▀░▀░▀
[/green]
"""

def clear_clipboard():
    
    try:
        pyperclip.copy("")
        console.print("[bold green]Буфер обміну успішно очищено![/bold green]")
    except pyperclip.PyperclipException:
        console.print("[bold red]Помилка: Не вдалося отримати доступ до буфера обміну.[/bold red]")
        console.print("Переконайтеся, що у вас встановлені необхідні бекенди (наприклад, xclip або xsel на Linux).")

def main_menu():
    
    while True:
        console.print("\n--- Меню очищення буфера обміну ---")
        console.print("[blue]1.[/blue] Очистити буфер обміну")
        console.print("[blue]2.[/blue] Вийти з програми")
        console.print("-----------------------------------")

        choice = input("Ваш вибір: ")

        if choice == "1":
            clear_clipboard()
        elif choice == "2":
            console.print("Вихід з програми. До побачення!")
            break
        else:
            console.print("[bold yellow]Невірний вибір. Будь ласка, введіть 1 або 2.[/bold yellow]")

if __name__ == "__main__":
    console.print(ASCII_ART)
    main_menu()
