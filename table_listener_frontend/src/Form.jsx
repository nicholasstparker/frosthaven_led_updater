import {useState} from "react";

function Radio({label, value, formType, handleChange}) {
    return (
        <div className="form-check">
            <input
                className="form-check-input"
                id={`radio${value}`}
                type="radio"
                name="radio"
                checked={formType === value}
                value={value}
                onChange={handleChange}
            />
            <label htmlFor={`radio${value}`} className="form-check-label">
                {label}
            </label>
        </div>
    );
}


function Radios({formType, handleChange}) {
    return (
        <fieldset>
            <legend>Form Type</legend>
            <Radio label="One" value="one" formType={formType} handleChange={handleChange}/>
            <Radio label="Two" value="two" formType={formType} handleChange={handleChange}/>
            <Radio label="Three" value="three" formType={formType} handleChange={handleChange}/>
        </fieldset>
    );
}

function Form() {
    const [formType, setFormType] = useState("one");

    function handleChange(event) {
        setFormType(event.target.value);
    }

    return (
        <div className="container text-center">
            <div className="row">
                <div className="col-4">
                </div>
                <div className="col-4">
                    <div className="card text-light shadow-lg rounded">
                        <ul className="nav nav-tabs" id="myTab" role="tablist">
  <li className="nav-item" role="presentation">
    <button className="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Home</button>
  </li>
  <li className="nav-item" role="presentation">
    <button className="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">Profile</button>
  </li>
  <li className="nav-item" role="presentation">
    <button className="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button" role="tab" aria-controls="contact-tab-pane" aria-selected="false">Contact</button>
  </li>
                            <li className="nav-item" role="presentation">
    <button className="nav-link" id="disabled-tab" data-bs-toggle="tab" data-bs-target="#disabled-tab-pane" type="button" role="tab" aria-controls="disabled-tab-pane" aria-selected="false" disabled>Disabled</button>
  </li>
</ul>
                        <div className="tab-content" id="myTabContent">
                            <div className="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabIndex="0">...</div>
                            <div className="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabIndex="0">...</div>
                            <div className="tab-pane fade" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabIndex="0">...</div>
                            <div className="tab-pane fade" id="disabled-tab-pane" role="tabpanel" aria-labelledby="disabled-tab" tabIndex="0">...</div>
</div>

                        <div className="p-3">
                        <form action="" method="get" className="form-example">
                            <h2>{formType}</h2>
                            <div className="form-floating mb-3">
                                <label htmlFor="name">Enter your name: </label>
                                <input type="text" className="form-control" name="name" id="name" required/>
                            </div>
                            <div className="form-floating mb-3">
                                <label htmlFor="email">Enter your email: </label>
                                <input type="email" className="form-control" name="email" id="email" required/>
                            </div>
                            {formType === "two" ? (
                                <div className="form-floating mb-3">
                                    <label htmlFor="emaila">skibide</label>
                                    <input type="email" className="form-control" name="emaila" id="emaila" required/>
                                </div>
                            ) : null}
                            <Radios formType={formType} handleChange={handleChange}/>
                            <div className="form-example">
                                <input className="btn btn-primary" type="submit" value="Subscribe!"/>
                            </div>
                        </form>
                        </div>
                    </div>
                </div>
                <div className="col-4">
                </div>
            </div>
        </div>
    );
}

export default Form;