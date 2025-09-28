# f1_eda_simple.py
# Requisitos: pandas, matplotlib  ->  pip install pandas matplotlib

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

# ===== CONFIG =====
CSV_PATH = r"f1.csv"  # ajuste aqui
OUT_DIR = Path("saida_f1")

def main():
    # 1) Leitura
    df = pd.read_csv(CSV_PATH, dtype=str)

    # 2) Padronização de colunas e tipos
    df.columns = (
        df.columns.str.strip().str.lower()
        .str.replace(" ", "_").str.replace(r"[^a-z0-9_]", "", regex=True)
    )
    # Conversões
    df["date"] = pd.to_datetime(df.get("date"), errors="coerce")
    df["year"] = pd.to_numeric(df.get("year"), errors="coerce", downcast="integer")
    df["laps"] = pd.to_numeric(df.get("laps"), errors="coerce")
    for c in ["continent","grand_prix","circuit","winner_name","team","time"]:
        if c in df.columns:
            df[c] = df[c].astype("string").str.strip()
    df["_race_td"] = pd.to_timedelta(df.get("time"), errors="coerce")
    df["_race_minutes"] = df["_race_td"].dt.total_seconds() / 60

    # 2) Tratamento dos nulos
    df = df.dropna(subset=["winner_name", "team", "year", "grand_prix"])
    df["continent"] = df["continent"].fillna("Unknown")

    # 3) Exploração: estatísticas simples
    total_corridas = int(df["grand_prix"].count())
    periodo = (int(df["year"].min()), int(df["year"].max()))
    circuitos = int(df["circuit"].nunique(dropna=True))
    pilotos_unicos = int(df["winner_name"].nunique(dropna=True))
    equipes_unicas = int(df["team"].nunique(dropna=True))
    laps_media = df["laps"].dropna().mean() if "laps" in df else None
    duracao_media_min = df["_race_minutes"].dropna().mean()

    top10_pilotos = df["winner_name"].value_counts().head(10)
    corridas_por_ano = df.groupby("year")["grand_prix"].count().sort_index()

    # 3) Visualizações
    OUT_DIR.mkdir(exist_ok=True, parents=True)

    # (a) Barras: Top 10 pilotos
    plt.figure(figsize=(8, 4.5))
    top10_pilotos.sort_values(ascending=True).plot(kind="barh")
    plt.title("Top 10 pilotos por vitórias")
    plt.xlabel("Vitórias"); plt.ylabel("Piloto")
    plt.grid(axis="x", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "top10_pilotos_vitorias.png", dpi=150)
    plt.close()

    # (b) Linha: GPs por ano
    if not corridas_por_ano.empty:
        plt.figure(figsize=(8, 4.5))
        corridas_por_ano.plot(kind="line", marker="o")
        plt.title("Número de GPs por ano")
        plt.xlabel("Ano")
        plt.ylabel("Quantidade de GPs")
        plt.grid(True, linestyle="--", linewidth=0.5)

        anos = range(int(corridas_por_ano.index.min()), int(corridas_por_ano.index.max()) + 1, 2)
        plt.xticks(anos, rotation=90)

        ax = plt.gca()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(2))

        # arredondar o limite superior para múltiplo de 5
        y_max = corridas_por_ano.max()
        limite_superior = int(math.ceil(y_max / 5.0)) * 5
        ax.set_ylim(0, limite_superior)

        plt.tight_layout()
        plt.savefig(OUT_DIR / "corridas_por_ano.png", dpi=150)
        plt.close()

    # 4) Relatório simples no console
    print("\n=== RELATÓRIO: F1 GRAND PRIX WINNERS (1950–2025) ===")
    print(f"Total de corridas       : {total_corridas}")
    print(f"Período coberto         : {periodo[0]}–{periodo[1]}")
    print(f"Circuitos únicos        : {circuitos}")
    print(f"Vencedores únicos       : {pilotos_unicos}")
    print(f"Equipes únicas          : {equipes_unicas}")
    print(f"Laps (média)            : {laps_media:.2f}" if laps_media is not None else "Laps (média)            : N/D")
    print(f"Duração média (min)     : {duracao_media_min:.2f}" if pd.notna(duracao_media_min) else "Duração média (min)     : N/D")
    print("\nTop 10 pilotos por vitórias:")
    for nome, qtd in top10_pilotos.items():
        print(f" - {nome}: {qtd}")
    print(f"\nGráficos salvos em: {OUT_DIR.resolve()}")
    print("Colunas:", df.columns.tolist())

if __name__ == "__main__":
    main()
