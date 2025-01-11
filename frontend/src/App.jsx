import { useAuthState } from 'react-firebase-hooks/auth'
import './App.css'
import { Route, Routes } from 'react-router';
import AuthGuard from './components/AuthGuard';
import { auth } from './firebase';
import Home from './routes/Home';
import Onboarding from './routes/Onboarding';
import NavBar from './components/NavBar/NavBar';
import Chat from './routes/Chat';
import Landing from './routes/Landing';
import LandingDemo from './routes/LandingDemo';
import TSignIn from './components/SignIn.jsx/TSignIn';
import TSignUp from './components/SignUp/TSignUp';

function App() {
  const [user, loading, error] = useAuthState(auth);

  return (
    <div className="h-screen">
      <NavBar />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/demo" element={<LandingDemo />} />
        <Route path="/home" element={AuthGuard(user, loading, <Home user={user}/>)} />
        <Route path="/sign-up" element={<TSignUp />} />
        <Route path="/sign-in" element={<TSignIn />} />
        <Route path="/sign-up/onboarding" element={AuthGuard(user, loading, <Onboarding />)} />
        <Route path="/chat" element={AuthGuard(user, loading, <Chat user={user}/>)} />
      </Routes>
    </div>
  )
}

export default App
