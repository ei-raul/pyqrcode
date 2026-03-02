# Gerador de QR Code HD

Aplicação web simples em Streamlit para gerar QR Codes em PNG com alta resolução, personalizando cor, fundo, nível de correção de erro e tamanho final.

## Funcionalidades

- Geração de QR Code a partir de URL.
- Personalização de cores (cor do QR Code e cor de fundo).
- Ajuste de resolução via `Box Size` (impacta no tamanho final da imagem).
- Seleção do nível de correção de erro (`L`, `M`, `Q`, `H`).
- Download direto do QR Code em formato `.png`.

## Stack

- Python `>=3.13`
- [Streamlit](https://streamlit.io/)
- [qrcode](https://pypi.org/project/qrcode/) com suporte a PIL (`qrcode[pil]`)

## Pré-requisitos

- [`uv`](https://docs.astral.sh/uv/) instalado na máquina.
- Python compatível (`>=3.13`).

## Instalação

No diretório do projeto, sincronize o ambiente com:

```bash
uv sync
```

Esse comando instala as dependências declaradas no `pyproject.toml` e usa o lockfile (`uv.lock`) para garantir versões reprodutíveis.

## Como executar

Inicie a aplicação com:

```bash
uv run streamlit run main.py
```

Após iniciar, abra a URL local exibida no terminal (normalmente `http://localhost:8501`).

## Como usar

1. Cole um link no campo principal.
2. Ajuste na barra lateral as cores, o tamanho do pixel (`Box Size`) e o nível de correção de erro.
3. Visualize o resultado gerado.
4. Clique em **Baixar QR Code (PNG)** para salvar o arquivo.

## Estrutura do projeto

```text
.
├── main.py           # Aplicação Streamlit
├── pyproject.toml    # Dependências e metadados do projeto
├── uv.lock           # Lockfile do uv
└── README.md
```

## Troubleshooting

- `uv: command not found`: instale o `uv` e tente novamente.
- Erro de versão do Python: confirme que está usando Python `>=3.13`.
- Porta do Streamlit em uso: execute com outra porta:

```bash
uv run streamlit run main.py --server.port 8502
```

## Melhorias futuras (opcional)

- Upload de logo para inserir no centro do QR Code.
- Histórico de links recentes gerados.
- Presets de estilo (cores e tamanhos).
