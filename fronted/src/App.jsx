import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [teams, setTeams] = useState([]);
  const [tournaments, setTournaments] = useState([]);
  const [cities, setCities] = useState([]);
  const [countries, setCountries] = useState([]);
  const [neutralOptions, setNeutralOptions] = useState([]);

  const [homeTeam, setHomeTeam] = useState("");
  const [awayTeam, setAwayTeam] = useState("");
  const [tournament, setTournament] = useState("");
  const [city, setCity] = useState("");
  const [country, setCountry] = useState("");
  const [neutral, setNeutral] = useState(false);

  const [prediction, setPrediction] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/teams")
      .then(res => setTeams(res.data.teams));

    axios.get("http://127.0.0.1:8000/tournaments")
      .then(res => setTournaments(res.data.tournaments));

    axios.get("http://127.0.0.1:8000/cities")
      .then(res => setCities(res.data.cities));

    axios.get("http://127.0.0.1:8000/countries")
      .then(res => setCountries(res.data.countries));

    axios.get("http://127.0.0.1:8000/neutral-options")
      .then(res => setNeutralOptions(res.data.neutral));
  }, []);

  const predictMatch = () => {
    axios.post("http://127.0.0.1:8000/predict", {
      home_team: homeTeam,
      away_team: awayTeam,
      tournament,
      city,
      country,
      neutral
    })
      .then(res => {
        setPrediction(res.data.prediction);
        setWinner(res.data.winner);
      })
      .catch(err => {
        console.log(err);
        alert("Prediction Failed");
      });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white flex flex-col items-center py-12 px-4">

      {/* Hero */}
      <div className="text-center mb-12">

        <div className="text-7xl mb-4">
          ⚽
        </div>

        <h1 className="text-6xl font-extrabold bg-gradient-to-r from-cyan-400 via-blue-400 to-green-400 bg-clip-text text-transparent">
          FIFA World Cup AI Predictor
        </h1>

        <p className="text-gray-300 text-xl mt-4">
          Predict international football matches using Machine Learning
        </p>

        <p className="text-gray-500 mt-2">
          React • FastAPI • Scikit-Learn
        </p>

      </div>

      {/* Form Card */}

      <div className="w-full max-w-lg bg-slate-800/70 backdrop-blur-lg rounded-3xl p-8 shadow-2xl border border-slate-700 space-y-5">

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={homeTeam}
          onChange={(e) => setHomeTeam(e.target.value)}
        >
          <option value="">🏠 Select Home Team</option>

          {teams.map(team => (
            <option key={team}>{team}</option>
          ))}

        </select>

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={awayTeam}
          onChange={(e) => setAwayTeam(e.target.value)}
        >
          <option value="">✈ Select Away Team</option>

          {teams.map(team => (
            <option key={team}>{team}</option>
          ))}

        </select>

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={tournament}
          onChange={(e) => setTournament(e.target.value)}
        >
          <option value="">🏆 Tournament</option>

          {tournaments.map(item => (
            <option key={item}>{item}</option>
          ))}

        </select>

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        >
          <option value="">📍 City</option>

          {cities.map(item => (
            <option key={item}>{item}</option>
          ))}

        </select>

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
        >
          <option value="">🌍 Country</option>

          {countries.map(item => (
            <option key={item}>{item}</option>
          ))}

        </select>

        <select
          className="w-full p-4 rounded-xl bg-slate-700 border border-slate-600"
          value={neutral}
          onChange={(e) => setNeutral(e.target.value === "true")}
        >
          {neutralOptions.map(option => (
            <option
              key={option.toString()}
              value={option}
            >
              {option ? "Neutral Venue" : "Home Venue"}
            </option>
          ))}

        </select>

        <button
          onClick={predictMatch}
          className="w-full bg-gradient-to-r from-blue-500 to-cyan-500 hover:scale-105 transition duration-300 rounded-xl p-4 text-xl font-bold shadow-xl"
        >
          🚀 Predict Match
        </button>

      </div>

      {prediction && (

        <div className="mt-10 w-full max-w-lg bg-slate-800 rounded-3xl p-8 shadow-2xl text-center">

          <h2 className="text-3xl font-bold mb-4">
            🏆 Prediction
          </h2>

          <p className="text-5xl font-extrabold text-green-400">
            {prediction}
          </p>

        </div>

      )}

    </div>
  );
}

export default App;