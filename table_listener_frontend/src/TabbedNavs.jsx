import React, { useState } from "react";
import Form from "./Form.jsx";

function TabbedNavs() {
  const [formType, setFormType] = useState("one");

  const tabs = [
    { id: "home-tab", target: "#home-tab-pane", ariaControls: "home-tab-pane", label: "One", type: "one" },
    { id: "profile-tab", target: "#profile-tab-pane", ariaControls: "profile-tab-pane", label: "Two", type: "two" },
    { id: "contact-tab", target: "#contact-tab-pane", ariaControls: "contact-tab-pane", label: "Three", type: "three" },
  ];

  return (
    <div className="container text-center">
      <div className="row">
        <div className="col-4">
          <div className="card text-light shadow-lg rounded">
            <ul className="nav nav-tabs" id="myTab" role="tablist">
              {tabs.map((tab, index) => (
                <li className="nav-item" role="presentation" key={tab.id}>
                  <button
                    className={`nav-link ${index === 0 ? "active" : ""}`}
                    id={tab.id}
                    data-bs-toggle="tab"
                    data-bs-target={tab.target}
                    type="button"
                    role="tab"
                    aria-controls={tab.ariaControls}
                    aria-selected={index === 0 ? "true" : "false"}
                    onClick={() => setFormType(tab.type)}
                  >
                    {tab.label}
                  </button>
                </li>
              ))}
            </ul>
            <div className="tab-content" id="myTabContent">
              {tabs.map((tab, index) => (
                <div
                  className={`tab-pane fade ${index === 0 ? "show active" : ""}`}
                  id={tab.ariaControls}
                  role="tabpanel"
                  aria-labelledby={tab.id}
                  tabIndex="0"
                  key={tab.ariaControls}
                >
                  <Form formType={formType} />
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TabbedNavs;
