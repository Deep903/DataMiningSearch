# DataMiningSearch
 Deployment Instructions:
 1. Go to pythonanywhere.com and create an account.
 2. Go into PA's (pythonanywhere) bash console and git clone the repository.
 3. In app.py remove the following lines of code:
    if __name__ == '__main__':
    app.run()
 4. In PA, go to the web tab, and create a new web app.
 5. Chose Manual configuration. NOT Flask. 
 6. A WSGI file in PA will be created. It will include instructions on what to comment out/add.
 7. Make sure the Web Tab in PA is pointing to the right directories.
 8. Click the "Reload" button.
 9. The web app should no be hosted and running on PA.
