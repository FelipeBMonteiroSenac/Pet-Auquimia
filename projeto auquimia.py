import tkinter as tk
from tkinter import messagebox # Importando caixa de mensagem (Pop-up)

def agendar_servico():
    # 1. Coleta de dados dos Widgets
    nome_dono = ent_dono.get()
    nome_pet = ent_pet.get()
    especie = var_especie.get()
    obs = txt_obs.get("1.0", "end") # Pega do caractere 1 ao final
    
    # Verificação simples
    if not nome_dono or not nome_pet:
        messagebox.showwarning("Atenção", "Preencha o nome do dono e do pet!")
        return

    # Coleta dos Checkbuttons
    servicos = []
    if var_banho.get(): servicos.append("Banho")
    if var_tosa.get(): servicos.append("Tosa")
    if var_unha.get(): servicos.append("Corte de Unha")
    
    msg_final = f"Cliente: {nome_dono}\nPet: {nome_pet} ({especie})\n"
    msg_final += f"Serviços: {', '.join(servicos)}\n"
    msg_final += f"Obs: {obs}"

    # Exibe resumo
    messagebox.showinfo("Agendamento Realizado!", msg_final)
    print("Dados salvos no sistema...") # Simulação de backend

# --- CONFIGURAÇÃO DA JANELA ---
root = tk.Tk()
root.title("Pet Shop AuQmia - Sistema de Agendamento")
root.geometry("500x550")
root.configure(bg="#f0f0f0") # Cor de fundo cinza claro

# --- 1. TÍTULO (Uso do PACK) ---
# O Pack é ótimo para cabeçalhos que ocupam toda a largura
header = tk.Label(root, text="🐾 Agendamento de Serviços", 
                  font=("Helvetica", 18, "bold"), bg="#4a90e2", fg="white", pady=10)
header.pack(fill="x")

# --- 2. FORMULÁRIO PRINCIPAL (Uso do FRAME + GRID) ---
# Usamos um Frame para agrupar o formulário e centralizá-lo
frame_form = tk.Frame(root, bg="#f0f0f0", pady=20)
frame_form.pack()

# -- Linha 0: Dono --
tk.Label(frame_form, text="Nome do Dono:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
ent_dono = tk.Entry(frame_form, width=30)
ent_dono.grid(row=0, column=1, padx=5, pady=5)

# -- Linha 1: Pet --
tk.Label(frame_form, text="Nome do Pet:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
ent_pet = tk.Entry(frame_form, width=30)
ent_pet.grid(row=1, column=1, padx=5, pady=5)

# --- 3. ESPÉCIE (Radiobutton) ---
tk.Label(frame_form, text="Espécie:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, sticky="ne", padx=5, pady=5)

# Frame interno para os Radiobuttons ficarem alinhados
frame_especie = tk.Frame(frame_form, bg="#f0f0f0")
frame_especie.grid(row=2, column=1, sticky="w")

var_especie = tk.StringVar(value="Cachorro") # Valor padrão
tk.Radiobutton(frame_especie, text="Cachorro", variable=var_especie, value="Cachorro", bg="#f0f0f0").pack(anchor="w")
tk.Radiobutton(frame_especie, text="Gato", variable=var_especie, value="Gato", bg="#f0f0f0").pack(anchor="w")

# --- 4. SERVIÇOS (Checkbutton com LabelFrame) ---
# LabelFrame cria uma borda com título ao redor das opções
grupo_servicos = tk.LabelFrame(root, text="Selecione os Serviços", font=("Arial", 10, "bold"), bg="#f0f0f0", padx=10, pady=10)
grupo_servicos.pack(fill="x", padx=20, pady=10)

var_banho = tk.BooleanVar()
var_tosa = tk.BooleanVar()
var_unha = tk.BooleanVar()

tk.Checkbutton(grupo_servicos, text="Banho Completo", variable=var_banho, bg="#f0f0f0").pack(anchor="w")
tk.Checkbutton(grupo_servicos, text="Tosa Higiênica", variable=var_tosa, bg="#f0f0f0").pack(anchor="w")
tk.Checkbutton(grupo_servicos, text="Corte de Unhas", variable=var_unha, bg="#f0f0f0").pack(anchor="w")

# --- 5. OBSERVAÇÕES (Widget Text) ---
tk.Label(root, text="Observações Adicionais:", bg="#f0f0f0").pack(anchor="w", padx=20)
txt_obs = tk.Text(root, height=4, width=50)
txt_obs.pack(padx=20, pady=5)

# --- 6. BOTÃO DE AÇÃO ---
btn_agendar = tk.Button(root, text="AGENDAR HORÁRIO", font=("Arial", 12, "bold"), 
                        bg="#4CAF50", fg="white", height=2, width=20, command=agendar_servico)
btn_agendar.pack(pady=20)

# --- 7. RODAPÉ (Uso do PLACE) ---
# O Place é usado aqui para fixar a versão no cantinho, independente do resto
footer = tk.Label(root, text="Sistema v1.0 - Dev Class", font=("Arial", 8), bg="#cccccc")
footer.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()
