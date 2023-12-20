import React, { useEffect, useState } from 'react';

interface jugador {
  first_name: string, 
  full_name: string, 
  id: number, 
  is_active: boolean, 
  last_name: string
}

function App() {
  const [data, SetData] = useState<jugador[]>([])

  useEffect(() => {
    fetch("/players").then(
      res => res.json()
    ).then(
      data => {
        SetData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div className="bg-red-600">
      {
        data?.map(player => (
          <p key={player.id}>
            {
              player?.full_name
            }
          </p>
        ))
      }
    </div>
  );
}

export default App;
