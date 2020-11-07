import Iframe from "react-iframe";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">State funding [EXPOSED]</header>
      <div className="App-body">
        <Iframe
          url="https://app.powerbi.com/reportEmbed?reportId=16570bb0-c7f9-4b72-b0a3-3ede822721a8&autoAuth=true&ctid=049e3382-8cdc-477b-9317-951b04689668&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXdlc3QtdXMtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D"
          width="1140px"
          height="541.25px"
          id="myId"
          className="myClassname"
          display="initial"
          position="relative"
          allowFullScreen="true"
        />
      </div>
    </div>
  );
}

export default App;
