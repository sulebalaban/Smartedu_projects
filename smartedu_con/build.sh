echo "Installing dependencies..."
pip install -r requirements.txt
pip install Pillow
echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput