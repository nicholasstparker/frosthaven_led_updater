import TabbedNavs from "./TabbedNavs.jsx";
import {useState} from 'react';
import { DatePickerInput } from '@mantine/dates';

function Container() {
    const [value, setValue] = useState < Date | null > (null);

    return (
        <div className="container text-center mt-3">
            <DatePickerInput
                label="Pick date"
                placeholder="Pick date"
                value={value}
                onChange={setValue}
            />
        </div>
    )
}

export default Container;
