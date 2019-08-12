import { Component, OnInit, NgModule } from '@angular/core';

import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';

@Component({
  selector: 'map',
  templateUrl: './index.html',
  styleUrls: ['./index.sass']
})

export class MapComponent implements OnInit {
  title = 'nearmap';

  map: Map;
  source: XYZ;
  layer: TileLayer;
  view: View;

  constructor() {
  }

  ngOnInit() {
    this.source = new XYZ({
      url: 'http://tile.osm.org/{z}/{x}/{y}.png'
    });

    this.layer = new TileLayer({
      source: this.source
    });

    this.view = new View({
      center: [0, 0],
      zoom: 3
    });

    this.map = new Map({
      target: 'map',
      layers: [this.layer],
      view: this.view
    });
  }
}
