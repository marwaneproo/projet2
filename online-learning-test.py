# ============================================
# PROJET PLATEFORME D'APPRENTISSAGE EN LIGNE
# SAISIE INTERACTIVE PAR L'UTILISATEUR
# ============================================
class Utilisateur:
    """Classe de base pour tous les utilisateurs"""
    
    def __init__(self, id, nom, prenom, date_naissance, email, mot_de_passe):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.date_inscription = "2024-01-15"
    
    def afficher_infos(self):
        print(f"\n--- Infos Utilisateur ---")
        print(f"ID: {self.id}")
        print(f"Nom: {self.nom} {self.prenom}")
        print(f"Email: {self.email}")
        print(f"Inscrit le: {self.date_inscription}")
    
    def se_connecter(self, email, mot_de_passe):
        if self.email == email and self.mot_de_passe == mot_de_passe:
            print(f"✓ Connexion réussie! Bonjour {self.prenom}")
            return True
        else:
            print("✗ Email ou mot de passe incorrect")
            return False


class Enseignant(Utilisateur):
    """Classe Enseignant héritant de Utilisateur"""
    
    def __init__(self, id, nom, prenom, date_naissance, email, mot_de_passe, specialite):
        super().__init__(id, nom, prenom, date_naissance, email, mot_de_passe)
        self.specialite = specialite
        self.biographie = ""
        self.cours_crees = []
    
    def createCours(self, titre, description, niveau, duree):
        """Créer un nouveau cours"""
        nouveau_cours = Cours(len(self.cours_crees) + 1, titre, description, niveau, duree)
        self.cours_crees.append(nouveau_cours)
        print(f"✓ Cours '{titre}' créé avec succès!")
        return nouveau_cours
    
    def evaluateApprenant(self, apprenant, note):
        """Évaluer un apprenant"""
        print(f"✓ Évaluation de {apprenant.prenom} {apprenant.nom}: {note}/20")
    
    def generateRapport(self):
        """Générer un rapport des cours"""
        print(f"\n--- Rapport des cours de {self.nom} {self.prenom} ---")
        print(f"Spécialité: {self.specialite}")
        print(f"Nombre de cours créés: {len(self.cours_crees)}")
        for cours in self.cours_crees:
            print(f"  - {cours.titre} (Niv. {cours.niveau_difficulte}/5)")


class Apprenant(Utilisateur):
    """Classe Apprenant héritant de Utilisateur"""
    
    def __init__(self, id, nom, prenom, date_naissance, email, mot_de_passe, niveau_etude):
        super().__init__(id, nom, prenom, date_naissance, email, mot_de_passe)
        self.niveau_etude = niveau_etude
        self.objectif = ""
        self.parcours_suivis = []
        self.progression = {}
    
    def passerEvaluation(self, evaluation):
        """Passer une évaluation"""
        print(f"✓ {self.prenom} passe l'évaluation: {evaluation.commentaire}")
        evaluation.calculateScore()
        evaluation.generateFeedback()
    
    def consulterRecommandations(self):
        """Afficher les recommandations"""
        print(f"\n--- Recommandations pour {self.prenom} ---")
        print(f"Niveau: {self.niveau_etude}")
        if self.objectif:
            print(f"Objectif: {self.objectif}")
        print("Cours suggérés: Python, HTML/CSS, SQL")
    
    def telechargerCertificat(self):
        """Télécharger un certificat"""
        certif = Certification(1, "2024-02-01", "ABC123XYZ")
        certif.genererPDF()
        certif.verifierAuthenticite()


class Cours:
    """Classe Cours"""
    
    def __init__(self, id_cours, titre, description, niveau_difficulte, duree):
        self.id_cours = id_cours
        self.titre = titre
        self.description = description
        self.niveau_difficulte = niveau_difficulte
        self.duree = duree
        self.modules = []
    
    def ajouterModule(self, titre, type_contenu, contenu, ordre):
        """Ajouter un module au cours"""
        nouveau_module = Module(len(self.modules) + 1, titre, type_contenu, contenu, ordre)
        self.modules.append(nouveau_module)
        print(f"  → Module '{titre}' ajouté au cours {self.titre}")
        return nouveau_module
    
    def modifierContenu(self, nouveau_titre, nouvelle_description):
        """Modifier le contenu du cours"""
        self.titre = nouveau_titre
        self.description = nouvelle_description
        print(f"✓ Cours modifié: {self.titre}")
    
    def publier(self):
        """Publier le cours"""
        print(f"✓ Cours '{self.titre}' publié avec {len(self.modules)} modules!")


class Module:
    """Classe Module"""
    
    def __init__(self, id_module, titre, type_contenu, contenu, ordre):
        self.id_module = id_module
        self.titre = titre
        self.type_contenu = type_contenu  # video, texte, quiz
        self.contenu = contenu
        self.ordre = ordre
        self.exercices = []
    
    def ajouterExercice(self, type_exo, enonce, difficulte, score_min):
        """Ajouter un exercice au module"""
        exercice = Exercice(len(self.exercices) + 1, type_exo, enonce, difficulte, score_min)
        self.exercices.append(exercice)
        print(f"    • Exercice ajouté au module '{self.titre}'")
        return exercice
    
    def getProgression(self):
        """Calculer la progression dans le module"""
        return f"Module '{self.titre}': {len(self.exercices)} exercices disponibles"


class Exercice:
    """Classe Exercice"""
    
    def __init__(self, id_exercice, type_exo, enonce, difficulte, score_minimum):
        self.id_exercice = id_exercice
        self.type = type_exo
        self.enonce = enonce
        self.difficulte = difficulte
        self.score_minimum = score_minimum
    
    def corriger(self, reponse_utilisateur, reponse_attendue):
        """Corriger l'exercice"""
        if reponse_utilisateur == reponse_attendue:
            print(f"  ✓ Exercice {self.id_exercice}: CORRECT! Score: {self.score_minimum}")
            return self.score_minimum
        else:
            print(f"  ✗ Exercice {self.id_exercice}: INCORRECT")
            return 0
    
    def adapterDifficulte(self, reussite):
        """Adapter la difficulté selon la réussite"""
        if reussite:
            self.difficulte = min(5, self.difficulte + 1)
            print(f"  ↑ Difficulté augmentée à {self.difficulte}/5")
        else:
            self.difficulte = max(1, self.difficulte - 1)
            print(f"  ↓ Difficulté diminuée à {self.difficulte}/5")


class Evaluation:
    """Classe Evaluation"""
    
    def __init__(self, id_evaluation, date_passation, commentaire):
        self.id_evaluation = id_evaluation
        self.date_passation = date_passation
        self.score = 0
        self.commentaire = commentaire
        self.reponses = {}
    
    def calculateScore(self):
        """Calculer le score de l'évaluation"""
        total = 0
        for question, reponse in self.reponses.items():
            if reponse == "correct":
                total += 1
        
        self.score = (total / max(1, len(self.reponses))) * 20
        print(f"  Score obtenu: {self.score:.1f}/20")
        return self.score
    
    def generateFeedback(self):
        """Générer un feedback"""
        if self.score >= 15:
            print(f"  ★ Feedback: Excellent travail! ★")
        elif self.score >= 10:
            print(f"  ✓ Feedback: Bon travail, continuez!")
        else:
            print(f"  ! Feedback: Vous pouvez mieux faire, révisez!")


class Certification:
    """Classe Certification"""
    
    def __init__(self, id_certificat, date_emission, code_validation):
        self.id_certificat = id_certificat
        self.date_emission = date_emission
        self.code_validation = code_validation
    
    def genererPDF(self):
        """Générer un PDF de certificat"""
        print(f"  📄 Certificat généré - ID: {self.id_certificat}")
        print(f"     Code validation: {self.code_validation}")
    
    def verifierAuthenticite(self):
        """Vérifier l'authenticité du certificat"""
        print(f"  🔒 Certificat authentique - Émis le {self.date_emission}")


class Administrateur(Utilisateur):
    """Classe Administrateur"""
    
    def __init__(self, id, nom, prenom, date_naissance, email, mot_de_passe, niveau_acces):
        super().__init__(id, nom, prenom, date_naissance, email, mot_de_passe)
        self.niveau_acces = niveau_acces
        self.utilisateurs = []
    
    def generateUtilisateurs(self):
        """Générer la liste des utilisateurs"""
        print(f"\n--- Liste des utilisateurs (Niveau: {self.niveau_acces}) ---")
        for user in self.utilisateurs:
            print(f"  - {user.prenom} {user.nom} ({user.email})")
    
    def configureSysteme(self):
        """Configurer le système"""
        print(f"✓ Configuration du système par {self.nom} {self.prenom}")
    
    def voirLogs(self):
        """Voir les logs"""
        print(f"--- Logs système ---")
        print("  [2024-02-01] Système démarré")
        print("  [2024-02-02] 3 nouveaux utilisateurs")
        print("  [2024-02-03] 2 cours publiés")


# ============================================
# PROGRAMME PRINCIPAL - SAISIE INTERACTIVE
# ============================================

print("=" * 60)
print("   PLATEFORME D'APPRENTISSAGE EN LIGNE")
print("=" * 60)

# ========== 1. SAISIE DES INFORMATIONS ENSEIGNANT ==========
print("\n" + "=" * 60)
print("📚 CRÉATION DU COMPTE ENSEIGNANT")
print("=" * 60)

id_ens = 1
nom_ens = input("Entrez le nom de l'enseignant: ")
prenom_ens = input("Entrez le prénom de l'enseignant: ")
date_naiss_ens = input("Entrez la date de naissance (AAAA-MM-JJ): ")
email_ens = input("Entrez l'email: ")
mdp_ens = input("Entrez le mot de passe: ")
specialite = input("Entrez la spécialité: ")

enseignant = Enseignant(id_ens, nom_ens, prenom_ens, date_naiss_ens, email_ens, mdp_ens, specialite)

biographie = input("Entrez une biographie (optionnel): ")
if biographie:
    enseignant.biographie = biographie

enseignant.afficher_infos()

# ========== 2. SAISIE DES INFORMATIONS APPRENANT ==========
print("\n" + "=" * 60)
print("🎓 CRÉATION DU COMPTE APPRENANT")
print("=" * 60)

id_app = 2
nom_app = input("Entrez le nom de l'apprenant: ")
prenom_app = input("Entrez le prénom de l'apprenant: ")
date_naiss_app = input("Entrez la date de naissance (AAAA-MM-JJ): ")
email_app = input("Entrez l'email: ")
mdp_app = input("Entrez le mot de passe: ")
niveau_etude = input("Entrez le niveau d'étude (ex: L1, L2, L3, Master): ")

apprenant = Apprenant(id_app, nom_app, prenom_app, date_naiss_app, email_app, mdp_app, niveau_etude)

objectif = input("Entrez l'objectif d'apprentissage (optionnel): ")
if objectif:
    apprenant.objectif = objectif

apprenant.afficher_infos()

# ========== 3. SAISIE DES INFORMATIONS ADMINISTRATEUR ==========
print("\n" + "=" * 60)
print("👑 CRÉATION DU COMPTE ADMINISTRATEUR")
print("=" * 60)

id_admin = 3
nom_admin = input("Entrez le nom de l'administrateur: ")
prenom_admin = input("Entrez le prénom de l'administrateur: ")
date_naiss_admin = input("Entrez la date de naissance (AAAA-MM-JJ): ")
email_admin = input("Entrez l'email: ")
mdp_admin = input("Entrez le mot de passe: ")
niveau_acces = input("Entrez le niveau d'accès (Admin, SuperAdmin): ")

admin = Administrateur(id_admin, nom_admin, prenom_admin, date_naiss_admin, email_admin, mdp_admin, niveau_acces)

# ========== 4. CONNEXION ==========
print("\n" + "=" * 60)
print("🔐 CONNEXION À LA PLATEFORME")
print("=" * 60)

print("\n--- Connexion Enseignant ---")
email_test = input("Email: ")
mdp_test = input("Mot de passe: ")
enseignant.se_connecter(email_test, mdp_test)

print("\n--- Connexion Apprenant ---")
email_test = input("Email: ")
mdp_test = input("Mot de passe: ")
apprenant.se_connecter(email_test, mdp_test)

# ========== 5. CRÉATION DE COURS PAR L'ENSEIGNANT ==========
print("\n" + "=" * 60)
print("📖 CRÉATION DE COURS")
print("=" * 60)

creer_cours = input("Voulez-vous créer un cours? (oui/non): ")

if creer_cours.lower() == "oui":
    titre_cours = input("Titre du cours: ")
    description_cours = input("Description du cours: ")
    niveau_cours = int(input("Niveau de difficulté (1-5): "))
    duree_cours = float(input("Durée du cours en heures: "))
    
    cours_python = enseignant.createCours(titre_cours, description_cours, niveau_cours, duree_cours)
    
    # ========== 6. AJOUT DE MODULES ==========
    print("\n--- AJOUT DE MODULES ---")
    nb_modules = int(input("Combien de modules voulez-vous ajouter? "))
    
    for i in range(nb_modules):
        print(f"\n--- Module {i+1} ---")
        titre_module = input("Titre du module: ")
        type_contenu = input("Type de contenu (video/texte/quiz): ")
        contenu = input("Contenu du module: ")
        ordre = i + 1
        
        module = cours_python.ajouterModule(titre_module, type_contenu, contenu, ordre)
        
        # ========== 7. AJOUT D'EXERCICES ==========
        ajouter_exo = input("Voulez-vous ajouter des exercices à ce module? (oui/non): ")
        
        if ajouter_exo.lower() == "oui":
            nb_exos = int(input("Nombre d'exercices à ajouter: "))
            
            for j in range(nb_exos):
                print(f"\n  Exercice {j+1}:")
                type_exo = input("  Type d'exercice (qcm/pratique): ")
                enonce = input("  Énoncé: ")
                difficulte = int(input("  Difficulté (1-5): "))
                score_min = float(input("  Score minimum: "))
                
                module.ajouterExercice(type_exo, enonce, difficulte, score_min)
    
    # ========== 8. PUBLICATION DU COURS ==========
    print("\n--- PUBLICATION ---")
    publier = input("Voulez-vous publier le cours? (oui/non): ")
    if publier.lower() == "oui":
        cours_python.publier()
    
else:
    # Création d'un cours par défaut si l'utilisateur ne veut pas créer
    print("Création d'un cours par défaut...")
    cours_python = enseignant.createCours(
        "Python pour Débutants",
        "Apprenez les bases de la programmation avec Python",
        2,
        20.5
    )
    
    module1 = cours_python.ajouterModule(
        "Variables et Types",
        "video",
        "Introduction aux variables en Python",
        1
    )
    
    module1.ajouterExercice(
        "qcm",
        "Quelle est la syntaxe correcte pour déclarer une variable?",
        1,
        10
    )
    
    cours_python.publier()

# ========== 9. ÉVALUATION ==========
print("\n" + "=" * 60)
print("📝 ÉVALUATION")
print("=" * 60)

evaluation = Evaluation(1, "2024-02-01", input("Commentaire pour l'évaluation: "))

print("\n--- Saisie des réponses ---")
nb_questions = int(input("Nombre de questions dans l'évaluation: "))

for i in range(nb_questions):
    question = input(f"Question {i+1}: ")
    reponse = input("Réponse (correct/incorrect): ")
    evaluation.reponses[question] = reponse

apprenant.passerEvaluation(evaluation)

# ========== 10. CORRECTION D'EXERCICES ==========
print("\n" + "=" * 60)
print("✏️ CORRECTION D'EXERCICES")
print("=" * 60)

if hasattr(cours_python, 'modules') and cours_python.modules:
    for module in cours_python.modules:
        if module.exercices:
            print(f"\n--- Module: {module.titre} ---")
            for exo in module.exercices:
                print(f"\nExercice: {exo.enonce}")
                rep_utilisateur = input("Votre réponse: ")
                rep_attendue = input("Réponse attendue: ")
                exo.corriger(rep_utilisateur, rep_attendue)
                
                adapter = input("Adapter la difficulté? (oui/non): ")
                if adapter.lower() == "oui":
                    reussite = input("L'apprenant a-t-il réussi? (oui/non): ")
                    exo.adapterDifficulte(reussite.lower() == "oui")

# ========== 11. ÉVALUATION PAR L'ENSEIGNANT ==========
print("\n" + "=" * 60)
print("⭐ ÉVALUATION DE L'APPRENANT")
print("=" * 60)

note = float(input("Note attribuée à l'apprenant (0-20): "))
enseignant.evaluateApprenant(apprenant, note)

# ========== 12. RECOMMANDATIONS ==========
print("\n" + "=" * 60)
print("💡 RECOMMANDATIONS")
print("=" * 60)

apprenant.consulterRecommandations()

# ========== 13. CERTIFICAT ==========
print("\n" + "=" * 60)
print("📜 CERTIFICAT")
print("=" * 60)

telecharger = input("Voulez-vous télécharger un certificat? (oui/non): ")
if telecharger.lower() == "oui":
    apprenant.telechargerCertificat()

# ========== 14. RAPPORT DE L'ENSEIGNANT ==========
print("\n" + "=" * 60)
print("📊 RAPPORT DE L'ENSEIGNANT")
print("=" * 60)

enseignant.generateRapport()

# ========== 15. ADMINISTRATION ==========
print("\n" + "=" * 60)
print("⚙️ ADMINISTRATION")
print("=" * 60)

admin.utilisateurs = [enseignant, apprenant]
admin.generateUtilisateurs()
admin.configureSysteme()
admin.voirLogs()

# ========== 16. RÉSUMÉ FINAL ==========
print("\n" + "=" * 60)
print("📋 RÉSUMÉ FINAL")
print("=" * 60)

print(f"\n✓ Enseignant: {enseignant.prenom} {enseignant.nom} - {enseignant.specialite}")
print(f"✓ Apprenant: {apprenant.prenom} {apprenant.nom} - {apprenant.niveau_etude}")
print(f"✓ Administrateur: {admin.prenom} {admin.nom} - {admin.niveau_acces}")

if hasattr(cours_python, 'modules'):
    print(f"\n✓ Cours créé: {cours_python.titre}")
    print(f"  - {len(cours_python.modules)} modules")
    total_exos = sum(len(module.exercices) for module in cours_python.modules)
    print(f"  - {total_exos} exercices")

print("\n" + "=" * 60)
print(" EXÉCUTION TERMINÉE AVEC SUCCÈS!")
print("=" * 60)
