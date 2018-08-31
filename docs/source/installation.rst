============
INSTALLATION
============


Requirements
------------

- Django 1.11 +
- jquery (jsTree requires 1.9.0 or greater in your webpage. You can use a CDN version or include a local copy.)

   .. highlight:: html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js"></script>


Création
--------

- Accès par le bouton :

.. image:: ./images/btn_add.png

Possibilité d’ajouter :
- Des administrateurs
- Des commerciaux
- Des contacts établissements

.. image:: ./images/form_access_add.png

- Une fois ajouté, un mail sera envoyé à l’adresse électronique précisée, contenant un lien permettant de définir un mot de passe et d’activer son compte.


Modification
------------

- Accès via le le bouton modifier à droite de chaque ligne représentant un accès.

.. image:: ./images/btn_edit_little.png

- Seuls les noms / prénoms / téléphone / fonction sont modifiables. Dans le cas contraire, il faut supprimer puis recréer l’accès.

.. image:: ./images/form_access_edit.png


Suppression
-----------

- Accès depuis le formulaire de modification d'un accès utilisateur.

.. warning::
   - La suppression d'un accès utilisateur supprimera toutes les références à l'utilisateur dans l'outil.
   - Pour désactiver l'accès d'un utilisateur snas le supprimer totalement, un administrateur peut se rendre sur l'interface d'administration, section 'utilisateurs', ouvrir l'utilisateur concerné, décocher la case 'actif' et enregistrer les modifications.