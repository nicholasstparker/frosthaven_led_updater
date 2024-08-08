// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import Form from "./Form.jsx";
// import TabbedNavs from "./TabbedNavs.jsx";
import Container from "./Container.jsx";
import { MantineProvider } from '@mantine/core';
import '@mantine/core/styles.css';

function App() {

  return (
    <MantineProvider>
        <Container />
    </MantineProvider>
  )
}

export default App
