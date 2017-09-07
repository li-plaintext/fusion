import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../shared';

@Component({
  selector: 'home-page',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  constructor(
    private userService: UserService
  ) {}

  getKeyWord: string = 'genome.one';

  ngOnInit() {
    this.userService.setAuth();
  }

  getComponentName() {
    let auth = this.userService.getAuth();
    return `${auth.firstName} ${auth.lastName}`;
  }

  getSum() {
    return '';
  }


}