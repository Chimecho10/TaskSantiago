import subprocess as sp

Nome_do_experimento = "Experimento X"
Versao_do_dataset = "Vx.0"

if __name__ == "__main__":
    modelo = "model.py"

    model_result = sp.run(["uv", "run", modelo])

    if model_result.returncode != 0:
        print("Erro ao executar o script:")
        print(model_result.stderr)
    else:
        print("Script executado com sucesso:")