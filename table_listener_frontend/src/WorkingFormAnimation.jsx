import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export const MyComponent = () => (
  <motion.div
    initial={{ opacity: 0, scale: 0.5 }}
    animate={{ opacity: 1, scale: 1 }}
    transition={{ duration: 0.5 }}
  />
);

function Form() {
  const [formType, setFormType] = useState("one");
  const [name, setName] = useState("");

  return (
    <div>
      <form action="" method="get" className="form-example">
        <h2>{formType}</h2>
        <div className="form-example">
          <label htmlFor="name">Enter your name: </label>
          <input
            type="text"
            name="name"
            id="name"
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="form-example">
          <label htmlFor="email">Enter your email: </label>
          <input type="email" name="email" id="email" required />
        </div>

        <AnimatePresence>
          {formType === "two" && (
            <motion.div
              key="extra-email"
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
              className="form-example"
            >
              <label htmlFor="emaila">Enter your email: </label>
              <input type="email" name="emaila" id="emaila" required />
            </motion.div>
          )}
        </AnimatePresence>

        <div>
          <fieldset>
            <legend>Form Type</legend>
            <label>
              <input
                type="radio"
                name="radio"
                checked={formType === "one"}
                value="one"
                onChange={() => setFormType("one")}
              />
              One
            </label>
            <label>
              <input
                type="radio"
                name="radio"
                checked={formType === "two"}
                value="two"
                onChange={() => setFormType("two")}
              />
              Two
            </label>
            <label>
              <input
                type="radio"
                name="radio"
                checked={formType === "three"}
                value="three"
                onChange={() => setFormType("three")}
              />
              Three
            </label>
          </fieldset>
        </div>
        <div className="form-example">
          <input type="submit" value="Subscribe!" />
        </div>
      </form>
    </div>
  );
}

export default Form;
