import {Container} from "@mantine/core";
import CustomTabs from "./CustomTabs";

export default function App() {
    const containerProps = {
        size: "sm",
    }
    return (
        <Container {...containerProps}>
            <CustomTabs />
        </Container>
    );
}