import "@mantine/core/styles.css";
import {MantineProvider, Container, Group, Textarea, Text, Switch, ColorPicker} from '@mantine/core';
import {useState} from "react";

export default function App() {
    const [consoleText, setConsoleText] = useState('');
    const [colorValue, setColorValue] = useState('rgb(0, 0, 0)');
    return <MantineProvider forceColorScheme={'dark'}>
        <Container size="sm" my="xl">
            <Group justify="center">
                <Switch label="Listener" size="xl" onLabel="On" offLabel="Off"/>
            </Group>
            <ColorPicker
                format="rgb"
                value={colorValue}
                onChange={setColorValue}
            />
            <Text>{colorValue}</Text>
            <Text mb="xs">Console Output:</Text>
            <Textarea
                value={consoleText}
                readOnly
                autosize
                minRows={10}
                maxRows={15}
                style={{fontFamily: 'monospace', backgroundColor: '#f5f5f5'}}
            />
        </Container>
    </MantineProvider>;
}
