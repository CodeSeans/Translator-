import customtkinter as ctk
from deep_translator import GoogleTranslator

# Uygulama stili: Light, Dark, System
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  # "green", "dark-blue", "blue"

# Ana pencere
app = ctk.CTk()
app.title("Modern Translator")
app.geometry("600x450")

# Dil listesi
lang_dict = {
    "English": "en",
    "Turkish": "tr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Russian": "ru",
    "Japanese": "ja",
    "Arabic": "ar",
}

# Girdi kutusu
input_label = ctk.CTkLabel(app, text="Enter text to translate:", anchor="w")
input_label.pack(padx=20, pady=(20, 5), fill="x")

input_text = ctk.CTkTextbox(app, height=100)
input_text.pack(padx=20, fill="x")

# Hedef dil seçimi
lang_label = ctk.CTkLabel(app, text="Target language:")
lang_label.pack(padx=20, pady=(10, 0), anchor="w")

lang_select = ctk.CTkOptionMenu(app, values=list(lang_dict.keys()))
lang_select.set("English")
lang_select.pack(padx=20, pady=5, fill="x")

# Çeviri sonucu
output_label = ctk.CTkLabel(app, text="Translation:")
output_label.pack(padx=20, pady=(10, 5), anchor="w")

output_text = ctk.CTkTextbox(app, height=100)
output_text.configure(state="disabled")  # sadece okunabilir
output_text.pack(padx=20, fill="x")

# Çeviri butonu
def translate():
    lang = lang_dict[lang_select.get()]
    src = input_text.get("1.0", "end").strip()
    try:
        translated = GoogleTranslator(source="auto", target=lang).translate(src)
        output_text.configure(state = "normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated)
        output_text.configure(state = "disabled")
    except Exception as e:
        output_text.configure(state = "normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", f"Error: {e}")
        output_text.configure(state = "disabled")

translate_button = ctk.CTkButton(app, text="Translate", command=translate)
translate_button.pack(pady=20)

# Başlat
app.mainloop()
