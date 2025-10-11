import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import './App.css'

function Home() {
  return <div className="container py-4"><h2>Home Feed</h2><p>Personalized posts will appear here.</p></div>
}

function Explore() {
  return <div className="container py-4"><h2>Explore</h2><p>Search and trending content.</p></div>
}

function Profile() {
  return <div className="container py-4"><h2>Profile</h2><p>User details and timeline.</p></div>
}

export default function App() {
  return (
    <BrowserRouter>
      <nav className="navbar navbar-expand navbar-light bg-light">
        <div className="container">
          <Link className="navbar-brand" to="/">Social</Link>
          <div className="navbar-nav">
            <Link className="nav-link" to="/">Home</Link>
            <Link className="nav-link" to="/explore">Explore</Link>
            <Link className="nav-link" to="/profile">Profile</Link>
          </div>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/explore" element={<Explore />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  )
}
