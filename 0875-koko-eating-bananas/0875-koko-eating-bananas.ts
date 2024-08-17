function minEatingSpeed(piles: number[], h: number): number {
        // left is equal to 1 (because need to eat at least 1 banana)
        let left: number = 1
        // right is equal to max(piles) - last index
        let right: number = Math.max(...piles);
        // res = right
        let res: number = right;

        // while left is less than or equal to right:
            // mid = left + right / 2
            // hours = 0
            // go to every pile:
            //     hours += Math.ceil(pile / mid)
            // if hours <= h:
            //      update res
            //      right = mid - 1 (search left portion)
            // else:
            //      left = mid + 1 (search for right portion)
        while (left <= right) {
            let mid: number = Math.floor((left + right) /2);
            let hours: number = 0;
            for (const pile of piles) {
                hours += Math.ceil(pile / mid);
            }
            if (hours <= h) {
                res = Math.min(res,mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }      

        // return res
        return res;
};