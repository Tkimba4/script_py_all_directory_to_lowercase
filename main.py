"""
    Script pour convertir tous les noms des dossieur contenu dans path en lowercase

"""

from pathlib import Path

try:
    user_path = input("Entrez le path complet du dossier - ")
    path = Path(user_path)
    if(path.exists()):
        for dir in path.rglob("*"):
            if dir.is_dir():
                suffix_part = str(dir).replace(f"{path}", "").lower()
                dir.rename(f"{path}{suffix_part}")
                #dir.rename()
                #fullpath = (str.lower(str(dir)))
                #sufix = str.lower("/".join(str(dir).split("/")))
                #prefix = "/".join(str(dir).split("/")[:5])
                #dir.rename(f"{prefix}/{sufix}") 
    else:
        print(f"Le chemin '{user_path}' n'est pas un chemin valide! ")
    
except Exception:
    print("Une erreur est survenu")

         

