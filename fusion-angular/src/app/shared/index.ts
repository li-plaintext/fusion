import { Injectable } from "@angular/core";


@Injectable()
export class UserService {
    private auth: any;


    setAuth() {
        this.auth = {
            firstName : 'Li',
            lastName: 'Xu'
        }
    }

    getAuth() {
        return this.auth;
    }

}