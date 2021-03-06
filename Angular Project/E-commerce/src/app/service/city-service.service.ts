import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { ApiService } from './api.service';
import { BaseService } from './base.service';

@Injectable({
  providedIn: 'root'
})
export class CityServiceService extends BaseService{
  private _urlCityList = 'city/get-list';

  constructor(private apiSrv:ApiService) {
    super(apiSrv);
  }

    /*This function returns the list of city object in paginated form */ 
  
   getCityList(paramsObject:any) : Observable<any> {
    console.log(paramsObject);
    return this.apiSrv.getData(this._urlCityList,paramsObject )
      .pipe(
        map(response => {
          console.log(response);
          return response;
        }),
        catchError(ex => {
          return ex;
        })
      );
    }
  }