import {useState} from "react";

function Form({ formType }) {

    return (
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
                {formType === "two" && (
                    <div className="form-floating mb-3">
                        <label htmlFor="emaila">skibide</label>
                        <input type="email" className="form-control" name="emaila" id="emaila"
                               required/>
                    </div>
                )}
                <div className="form-example">
                    <input className="btn btn-primary" type="submit" value="Subscribe!"/>
                </div>
            </form>
        </div>
    );
}

export default Form;