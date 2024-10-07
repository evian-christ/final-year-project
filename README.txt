This is a readme file that guide you through the project directory.

PROJECT
	-futforall
	-Documents
	-diary.txt
	-Project Plan.docx
	-Project Report.docx
	-README.txt

The project root folder consists of 2 folders and some documents.
the folder 'futforall' is the software folder for the project.
the folder 'Documents' is where all the electronic copies of submitted documents are located. (Project report.pdf)
Project plan in docx form, diary, and the project report in docx form is in the root folder of the project.

Inside the futforall folder (only the notable files included below)
The structure of the project files are in the final report as well.

futforall
	-docs
		--_build
			---html
				----index.html
	-futforall (config folder)
		--settings.py
		--urls.py
		--views.py*
		--consumers.py*
		--routing.py
	-account
		--forms.py
		--models.py
		--urls.py
		--views.py*
	-match
		--admin.py
		--forms.py
		--models.py
		--urls.py
		--views.py*
	-notifc
		--urls.py
		--views.py
		--models.py
	-templates
		--account
			---login.html
			---profile.html
			---signup.html
		--match
			---create.html
			---detail.html
		--notifc
			---index.html*
		--base.html
		--base(nav).html
		--form_errors.html
		--index.html*

Although all of the files are worth looking into, some files required more effort than the other ones. I have marked them with an asterick in the above list.

The documentation is far from completed, but you can view it in futforall/docs/_build/html/index.html

For insturctions on how to run the software, please read Chapter 7 of the project report.

Thank you!

