import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'home-page',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  getKeyWord: string = 'angular';

  ngOnInit() {}

  getComponentName() {
    return 'home';
  }
}