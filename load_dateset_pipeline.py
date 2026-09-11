import subprocess as sp

dvc_pull_result = sp.run(["dvc", "pull", "--force"], 
                         capture_output=True, 
                         text=True)

if dvc_pull_result.returncode != 0:
    print("Erro ao executar o DVC PULL:")
    print(dvc_pull_result.stderr)
else:
    print("DVC PULL executado com sucesso:")

dvc_checkout_result = sp.run(["dvc", "checkout", "--force"], 
                      capture_output=True, 
                      text=True)

if dvc_checkout_result.returncode != 0:
    print("Erro ao executar o DVC CHECKOUT:")
    print(dvc_checkout_result.stderr)
else:
    print("DVC CHECKOUT executado com sucesso:")