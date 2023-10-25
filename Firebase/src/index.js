// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDNIuskOXgQgfTpG25sfjbbyg-0ZZagki8",
  authDomain: "mvptracking-705b5.firebaseapp.com",
  projectId: "mvptracking-705b5",
  storageBucket: "mvptracking-705b5.appspot.com",
  messagingSenderId: "848079275697",
  appId: "1:848079275697:web:138458361a02563863c490",
  measurementId: "G-QL9PTJ10FL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
console.log(analytics)