import React from 'react';
import MapView from './MapView';
import UploadForm from './UploadForm';

function App() {
  return (
    <div>
      <h1>LTE Tower Optimizer</h1>
      <UploadForm />
      <MapView />
    </div>
  );
}

export default App;
