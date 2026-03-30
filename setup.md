\# Django Project Setup Instructions



Follow these steps to run the project locally.



1\. Clone the repository:

&nbsp;  ```

&nbsp;  git clone https://github.com/GregLapus/django-portfolio.git

&nbsp;  cd django-portfolio

&nbsp;  ```



2\. Create a virtual environment:

&nbsp;  ```

&nbsp;  python -m venv venv

&nbsp;  ```



3\. Activate the virtual environment:

&nbsp;  - Windows (CMD):

&nbsp;    ```

&nbsp;    venv\\Scripts\\activate

&nbsp;    ```

&nbsp;  - macOS/Linux:

&nbsp;    ```

&nbsp;    source venv/bin/activate

&nbsp;    ```



4\. Install dependencies:

&nbsp;  ```

&nbsp;  pip install -r requirements.txt

&nbsp;  ```



5\. Apply migrations:

&nbsp;  ```

&nbsp;  python manage.py migrate

&nbsp;  ```



6\. Run the server:

&nbsp;  ```

&nbsp;  python manage.py runserver

&nbsp;  ```



7\. Open in browser:

&nbsp;  ```

&nbsp;  http://127.0.0.1:8000/

&nbsp;  ```



Optional: To deactivate the environment:

```

deactivate

```

