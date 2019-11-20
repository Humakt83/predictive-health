cd backend/db
./stop_start.sh &
cd ..
./stop_start.sh &
cd ../frontend-client
yarn serve &
cd ../frontend-doctor
yarn serve &
cd ..