// import { Button, Checkbox, Group, Tabs, TextInput } from "@mantine/core";
// import { useForm } from '@mantine/form';
// import { useState } from "react";
// import { DatePickerInput } from "@mantine/dates";
//
// export default function CustomTabs() {
//   const form = useForm({
//     initialValues: {
//       email: '',
//       termsOfService: false,
//       date: null,
//     },
//     validate: {
//       email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Invalid email'),
//     },
//   });
//
//   const handleDateChange = (date: Date | null) => {
//     form.setFieldValue('date', date);
//   };
//
//   return (
//     <Tabs variant="outline" defaultValue="gallery">
//       <Tabs.List>
//         <Tabs.Tab value="gallery">Gallery</Tabs.Tab>
//         <Tabs.Tab value="messages">Messages</Tabs.Tab>
//       </Tabs.List>
//
//       <Tabs.Panel value="gallery">
//         <form onSubmit={form.onSubmit((values) => console.log(values))}>
//           <TextInput
//             withAsterisk
//             label="Email"
//             placeholder="your@email.com"
//             {...form.getInputProps('email')}
//           />
//           <DatePickerInput
//             label="Pick date"
//             placeholder="Pick date"
//             value={form.values.date}
//             onChange={handleDateChange}
//           />
//           <Checkbox
//             mt="md"
//             label="I agree to sell my privacy"
//             {...form.getInputProps('termsOfService', { type: 'checkbox' })}
//           />
//           <Group justify="flex-end" mt="md">
//             <Button type="submit">Submit</Button>
//           </Group>
//         </form>
//       </Tabs.Panel>
//
//       <Tabs.Panel value="messages">
//         <form onSubmit={form.onSubmit((values) => console.log(values))}>
//           <TextInput
//             withAsterisk
//             label="Email"
//             placeholder="your@email.com"
//             {...form.getInputProps('email')}
//           />
//           <DatePickerInput
//             label="Pick date"
//             placeholder="Pick date"
//             value={form.values.date}
//             onChange={handleDateChange}
//           />
//           <Checkbox
//             mt="md"
//             label="I agree to sell my privacy"
//             {...form.getInputProps('termsOfService', { type: 'checkbox' })}
//           />
//           <Group justify="flex-end" mt="md">
//             <Button type="submit">Submit</Button>
//           </Group>
//         </form>
//       </Tabs.Panel>
//     </Tabs>
//   );
// }
