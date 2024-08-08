import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
import {MantineProvider} from '@mantine/core';
import {theme} from './theme';
import Container from './Container';


export default function App() {

    return (
        <MantineProvider theme={theme}>
            <Container />
        </MantineProvider>
    );
}
